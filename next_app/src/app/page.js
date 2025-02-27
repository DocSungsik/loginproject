import { AuthSession } from "@/lib/AuthSession";
import { LoginButton } from './loginbutton';

export default function Home() {
  return (
    <>
    <AuthSession><LoginButton></LoginButton></AuthSession>
    <h2>Hello</h2>
    </>
  );
}
