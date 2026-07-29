import type { Metadata } from "next";

export const metadata: Metadata = {
  title: "altr | Tampa AI Enablement and Automation",
  description:
    "Tampa-based AI enablement and automation studio for practical AI workshops, workflow automations, custom agents, and coding-agent systems.",
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en">
      <body>{children}</body>
    </html>
  );
}
