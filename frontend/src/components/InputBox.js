'use client'
import { ArrowUp } from "lucide-react";
import { useState } from "react";

export default function InputBox() {

    const [text, setText] = useState("");
    
    const handleFormSubmit = async (e) => {
        e.preventDefault();
    }
    
    return <form onSubmit={handleFormSubmit} className="bg-foreground overflow-hidden px-3 pl-7 py-3 w-1/2 flex justify-between items-center rounded-3xl">
        <input value={text} o onChange={(e) => { setText(e.target.value) }} className="bg-foreground h-10 outline-none flex-1 text-white" placeholder="Ask anything..." />
        <button className="bg-white h-9 w-9 rounded-full flex justify-center hover:bg-gray-400 transition-colors items-center">
            <ArrowUp className="" size={22} />
        </button>
    </form>
}