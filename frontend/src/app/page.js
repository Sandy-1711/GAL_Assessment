'use client'
import { useSelector } from "react-redux"
import { useDispatch } from "react-redux"
import { addMessage, clear } from "../../redux/features/chatSlice";
import InputBox from "@/components/InputBox";

export default function Home() {
  const dispatch = useDispatch();
  const chat = useSelector(state => state.chat).value
  return <div className="h-screen w-screen bg-background">
    <InputBox numberOfMessages={chat?.messages?.length} />
  </div>
}
