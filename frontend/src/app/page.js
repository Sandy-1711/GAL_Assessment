'use client'
import { useSelector } from "react-redux"
export default function Home() {

  const chat = useSelector(state => state.chat).value
  console.log(chat.messages)
  return <div className="h-screen w-screen bg-white">

  </div>
}
