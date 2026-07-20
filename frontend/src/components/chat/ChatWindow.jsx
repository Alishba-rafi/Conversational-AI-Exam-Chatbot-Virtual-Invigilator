import { useState, useRef, useEffect } from "react";
import MessageList from "./MessageList";
import ChatInput from "./ChatInput";
import "../../style/ChatWindow.css";

function ChatWindow() {
  const [messages, setMessages] = useState([
    {
      id: 1,
      text: "Hello! I'm your Student Chatbot.",
      sender: "bot",
    },
  ]);

  const [loading, setLoading] = useState(false);

  const bottomRef = useRef(null);

  useEffect(() => {
    bottomRef.current?.scrollIntoView({
      behavior: "smooth",
      block: "end",
    });
  }, [messages, loading]);

  const handleSend = async (text) => {
    if (!text.trim()) return;

    const userMessage = {
      id: Date.now(),
      text,
      sender: "user",
    };

    setMessages((prev) => [...prev, userMessage]);

    setLoading(true);

    try {
      const response = await fetch("http://127.0.0.1:8000/chat", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          question: text,
        }),
      });

      const data = await response.json();

      if (!response.ok) {
        throw new Error(data.detail || "Something went wrong.");
      }

      const botMessage = {
        id: Date.now() + 1,
        text: data.answer,
        sender: "bot",
      };

      setMessages((prev) => [...prev, botMessage]);
    } catch (error) {
  console.error(error);

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