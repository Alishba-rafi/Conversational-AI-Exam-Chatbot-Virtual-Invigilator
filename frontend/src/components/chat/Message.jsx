function Message({ text, sender }) {
  const isUser = sender === "user";

  return (
    <div
      className={`d-flex mb-3 ${
        isUser ? "justify-content-end" : "justify-content-start"
      }`}
    >
      <div
        className={`p-3 rounded ${
          isUser ? "bg-primary text-white" : "bg-light border"
        }`}
        style={{ maxWidth: "70%" }}
      >
       {text}
      </div>
    </div>
  );
}

export default Message;