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