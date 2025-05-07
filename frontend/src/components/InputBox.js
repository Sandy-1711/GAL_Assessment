'use client'
import { ArrowUp, LoaderCircle } from "lucide-react";
import { useState } from "react";
import { useDispatch } from "react-redux";
import { addMessage } from "../../redux/features/chatSlice";
import useSendChat from "../../hooks/sendChatHook";


export default function InputBox({ lengthOfMessages }) {

    const { data, loading, sendMessage } = useSendChat();
    const [text, setText] = useState("");
    const [customerId, setCustomerId] = useState("");
    const dispatch = useDispatch();

    const handleFormSubmit = async (e) => {
        e.preventDefault();

        dispatch(
            addMessage({
                user: "self",
                message: text
            })
        )
        let temporaryMessageHolder = text; // for ui purposes
        setText("");
        // return
        await sendMessage({
            message: temporaryMessageHolder,
            conversation_id: "optional-conversation-id",
            customer_id: customerId,
            metadata: {}
        })
    }

    return <form style={{
        position: lengthOfMessages > 0 && "fixed",
        transition: "0.5s linear",
        bottom: lengthOfMessages > 0 && "2.5rem",
        maxWidth: lengthOfMessages > 0 && "48rem",
        width: lengthOfMessages > 0 && "66.66667%"

    }} onSubmit={handleFormSubmit} className={` bg-foreground overflow-hidden px-3 pl-7 py-3 w-1/3 flex justify-between items-center rounded-3xl`}>
        <input value={text} onChange={(e) => { setText(e.target.value) }} className="bg-foreground h-10 outline-none flex-1 text-white" placeholder="Ask anything..." />
        <button disabled={loading} className="bg-white h-9 w-9 rounded-full flex justify-center hover:bg-gray-400 transition-colors items-center">
            {loading ?
                <LoaderCircle className="animate-spin" size={22} />
                :
                <ArrowUp className="" size={22} />
            }
        </button>
    </form>
}