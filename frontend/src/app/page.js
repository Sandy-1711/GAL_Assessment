'use client'
import { useSelector } from "react-redux"
import { useDispatch } from "react-redux"
import { addMessage, clear } from "../../redux/features/chatSlice";
import InputBox from "@/components/InputBox";
import ChatMessagesBox from "@/components/ChatMessagesBox";

export default function Home() {
  const dispatch = useDispatch();
  const chat = useSelector(state => state.chat).value;
  let lengthOfMessages = chat?.messages?.length;
  return <div className="h-screen w-screen bg-background flex justify-center items-center">
    {lengthOfMessages > 0 && <ChatMessagesBox messages={chat.messages} />}
    <InputBox numberOfMessages={chat?.messages?.length} />
  </div>
}
