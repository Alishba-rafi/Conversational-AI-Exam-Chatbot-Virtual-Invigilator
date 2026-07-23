import { useState, useRef, useEffect } from "react";
import MessageList from "./MessageList";
import ChatInput from "./ChatInput";
import "../../style/ChatWindow.css";

function ChatWindow() {
  const studentId = Number(localStorage.getItem("student_id"));
  const [messages, setMessages] = useState([
    {
      id: 1,
      text: "Hello! I'm your Student Chatbot.",
      sender: "bot",
    },
  ]);

  const [loading, setLoading] = useState(false);
// To automatically scroll when a new message arriv
  const bottomRef = useRef(null);

  //Every new message automatically scrolls into view. when message and loadind state change 
  useEffect(() => {
    bottomRef.current?.scrollIntoView({
      behavior: "smooth",
      block: "end",
    });
  }, [messages, loading]);

  const handleSend = async (text) => {
    if (!text.trim()) return;

    // tostore every time different id in array of message we use date.now()
    const userMessage = {
      id: Date.now(),
      text,
      sender: "user",
    };

    setMessages((prev) => [...prev, userMessage]);

    setLoading(true);
    console.log("Student ID:", studentId);
    console.log("Question:", text);

    try {
const response = await fetch("http://127.0.0.1:8000/chat", {
  method: "POST",
  headers: {
    "Content-Type": "application/json",
  },
  body: JSON.stringify({
    student_id: studentId,
    question: text,
  }),
});

if (!response.ok) {
  throw new Error("Something went wrong.");
}
//to get pice
const reader = response.body.getReader();
// browser recive bytes not text 
const decoder = new TextDecoder();

let botText = "";

// Create an empty bot message
const botId = Date.now() + 1;
    //Take all the existing messages, append the new message,
//  save the new array as the state, and let React update 
// the chat UI automatically.

// create a empty  message to display intially 
setMessages((prev) => [
  ...prev,
  {
    id: botId,
    text: "",
    sender: "bot",
  },
]);

while (true) {
  const { done, value } = await reader.read();

  if (done) break;

  botText += decoder.decode(value);

  setMessages((prev) =>
    prev.map((msg) =>
      msg.id === botId
        ? { ...msg, text: botText } // ...means copy all the previous message and update the text into bottext
        : msg
    )
  );
}
    } catch (error) {
  console.log(error);

  setMessages((prev) => [
    ...prev,
    {
      id: Date.now(),
      text: "Sorry, I'm unable to answer right now. Please try again later.",
      sender: "bot",
    },
  ]);
} finally {
      setLoading(false);
    }
  };

  return (
    <div className="chat-window">
      <div className="message-area">
        <MessageList
          messages={messages}
          loading={loading}
        />

        <div ref={bottomRef} />
      </div>

      <ChatInput
        onSend={handleSend}
        disabled={loading}
      />
    </div>
  );
}

export default ChatWindow;