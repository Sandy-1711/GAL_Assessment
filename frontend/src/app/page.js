'use client'
import { useSelector } from "react-redux"
import { useDispatch } from "react-redux"
import { addMessage, clear } from "../../redux/features/chatSlice";

export default function Home() {
  const dispatch = useDispatch();
  const chat = useSelector(state => state.chat).value
  return <div className="h-screen w-screen bg-background">
    
  </div>
}
