import assert from 'node:assert/strict';
import { readFileSync } from 'node:fs';
import { test } from 'node:test';
import vm from 'node:vm';

const script = readFileSync(new URL('../call-now.js', import.meta.url), 'utf8');

function setup(hostname, response) {
  const fields = {
    name: 'Alex Example',
    email: 'alex@example.com',
    phone: '+15555550123',
    company: 'Example & Co',
    notes: 'Automate intake + review',
    consent: 'on'
  };
  const status = { textContent: '', dataset: {} };
  const submit = { disabled: false };
  let handler;
  const form = {
    reportValidity: () => true,
    querySelector: (selector) => selector === 'button[type="submit"]' ? submit : { value: 'turnstile-test-token' },
    addEventListener: (_event, callback) => { handler = callback; }
  };
  const requests = [];
  const context = {
    document: { getElementById: (id) => id === 'call-now-form' ? form : status },
    window: { location: { hostname } },
    FormData: class { get(key) { return fields[key]; } },
    Intl,
    fetch: async (url, options) => {
      requests.push({ url, options });
      return response;
    }
  };
  vm.runInNewContext(script, context);
  return { fields, status, submit, requests, send: () => handler({ preventDefault() {} }) };
}

test('localhost preview does not request a real call', async () => {
  const page = setup('127.0.0.1');
  await page.send();
  assert.equal(page.requests.length, 0);
  assert.match(page.status.textContent, /preview will not place a call/);
});

test('live form sends required JSON and displays endpoint message', async () => {
  const page = setup('altrwork.com', { ok: true, json: async () => ({ ok: true, message: 'Your call is on its way.' }) });
  await page.send();
  assert.equal(page.requests.length, 1);
  assert.equal(page.requests[0].url, 'https://kara-intake.weathered-boat-4f14.workers.dev/call-now');
  assert.equal(page.requests[0].options.method, 'POST');
  assert.equal(page.requests[0].options.headers['Content-Type'], 'application/json');
  assert.deepEqual(JSON.parse(page.requests[0].options.body), {
    ...page.fields,
    consent: true,
    timeZone: Intl.DateTimeFormat().resolvedOptions().timeZone,
    turnstileToken: 'turnstile-test-token'
  });
  assert.equal(page.status.textContent, 'Your call is on its way.');
  assert.equal(page.status.dataset.state, 'success');
  assert.equal(page.submit.disabled, false);
});

test('www live domain also permits the call request', async () => {
  const page = setup('www.altrwork.com', { ok: true, json: async () => ({ ok: true, message: 'Your call is on its way.' }) });
  await page.send();
  assert.equal(page.requests.length, 1);
});

test('endpoint errors are shown to the visitor', async () => {
  const page = setup('altrwork.com', { ok: false, json: async () => ({ ok: false, message: 'Calls are unavailable right now.' }) });
  await page.send();
  assert.equal(page.status.textContent, 'Calls are unavailable right now.');
  assert.equal(page.status.dataset.state, 'error');
});
