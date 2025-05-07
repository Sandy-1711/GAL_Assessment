import React from "react";
import { Bot, User } from "lucide-react";

export default function ChatMessagesBox({ messages = [] }) {
    return (
        <div className="p-4 max-w-3xl mx-auto  space-y-2">
            {messages.map((msg, index) => (
                <div
                    key={index}
                    className={`flex items-start space-x-2 ${msg.user === "self" ? "justify-end" : "justify-start"
                        }`}
                >
                    {msg.user === "ai" && (
                        <Bot className="w-5 h-5 mt-1 text-gray-500" />
                    )}
                    <div
                        className={`rounded-2xl px-4 py-2 text-base whitespace-pre-wrap leading-6 max-w-[75%] ${msg.user === "self"
                            ? "bg-foreground text-white"
                            : "bg-foreground text-white"
                            }`}
                    >
                        {msg.message}
                    </div>
                    {msg.user === "self" && (
                        <User className="w-4 h-4 mt-1 text-blue-500" />
                    )}
                </div>
            ))}
        </div>
    );
};

