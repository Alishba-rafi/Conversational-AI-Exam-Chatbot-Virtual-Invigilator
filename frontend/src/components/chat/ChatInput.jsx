import { useState } from "react";

function ChatInput({ onSend }) {
  const [message, setMessage] = useState("");

  const handleSend = () => {
    if (message.trim() === "") return; // Don't send empty messages

    onSend(message);
    setMessage("");
  };

  return (
    <div className="border-top p-3 d-flex gap-2">
      <input
        type="text"
        className="form-control"
        placeholder="Type your message..."
        value={message}
        onChange={(e) => setMessage(e.target.value)}
        onKeyDown={(e) => {
          if (e.key === "Enter") {
            handleSend();
          }
        }}
      />

      <button
        className="btn btn-primary"
        onClick={handleSend}
      >
        Send
      </button>
    </div>
  );
}

export default ChatInput;