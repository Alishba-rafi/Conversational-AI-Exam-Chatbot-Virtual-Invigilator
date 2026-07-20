// import Navbar from "./Navbar";
// import Sidebar from "./Sidebar";
// import ChatWindow from "../chat/ChatWindow";

// function MainLayout() {
//   return (
//    <div className="container-fluid vh-100 p-0">
//     <div className="row h-100 g-0">

//         {/* Sidebar */}
//         <div className="col-3 border-end">
//           <Sidebar />
//         </div>

//         {/* Main Content */}
//        <div className="col-9 d-flex flex-column p-0">
//           <Navbar />

//          <div className="flex-grow-1 d-flex">
//          <ChatWindow />
//          </div>

//         </div>

//       </div>
//     </div>
//   );
// }

// export default MainLayout;



import Navbar from "./Navbar";
import Sidebar from "./Sidebar";
import ChatWindow from "../chat/ChatWindow";
import "../../style/MainLayout.css";


function MainLayout(){

return(

<div className="main-layout">


<div className="sidebar-container border-end">

<Sidebar />

</div>



<div className="main-content">

<Navbar />


<div className="chat-container">

<ChatWindow />

</div>


</div>


</div>

);

}


export default MainLayout;