import { AuthSession } from "@/lib/AuthSession";


export default function RootLayout({ children }) {
    return (
      <AuthSession>{children}</AuthSession>
    );
  }