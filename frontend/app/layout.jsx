import "./globals.css";
import Navbar from "@/components/common/Navbar";

export const metadata = {
  title: "GitGrade",
  description: "AI-powered GitHub Repository Analyzer",
};

export default function RootLayout({ children }) {
  return (
    <html lang="en">
      <body>
        {children}
      </body>
    </html>
  );
}