import { NextAuthOptions } from "next-auth";
import CredentialsProvider from "next-auth/providers/credentials";
import api from "@/lib/api"

export const authOptions : NextAuthOptions = {
    providers: [
        CredentialsProvider({
            name: "Credentials",
            credentials: {
                email: {label: "Email", type: "email", placeholder: "user@example.com"},
                password: {label: "Password", type: "password"},
            },
            async authorize(credentials) {
                try {
                    const response = await api.post("login", new URLSearchParams({
                        username: credentials.email,
                        password: credentials.password
                    }), {headers: {"Content-Type": "application/x-www-form-urlencoded"}, withCredentials: true});

                    const user = response.data;
                    if (user) {
                        return { id: user.access_token, name: credentials.email };
                    }
                } catch (error) {
                    console.error("Login failed:", error);
                    return null;
                }
            }
        })
    ],
    callbacks: {
        async jwt({token, user}){
            if (user) {token.user = user;}
            return token;
        },
        async session({ session, token }) {
            if (token.user) {session.user = token.user;}
            return session;
        },
    },
    pages: {
        signIn: "/login"
    },
    secret: process.env.NEXTAUTH_SECRET,
    session: {
        strategy: "jwt",
        maxAge: 60 * 60
    },
};