import Message from "./Message";

function MessageList({ messages, loading }) {
  return (
    <>
      {messages.map((message) => (
        <Message
          key={message.id}
          text={message.text}
          sender={message.sender}
        />
      ))}

      {loading && (
        <Message
          text="Typing..."
          sender="bot"
        />
      )}
    </>
  );
}

export default MessageList;