import "./globals.css";

export const metadata = {
  title: "Blog Post Helper",
  description: "Draft projects, capture sources, and extract claims.",
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="en">
      <body>
        {children}
      </body>
    </html>
  );
}
