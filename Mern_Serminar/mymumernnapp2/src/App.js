import AboutFun from "./Component/AboutFun";
import ContectFun from "./Component/ContectFun";
import FooterFun from "./Component/FooterFun";
import HeaderFun from "./Component/HeaderFun";
import HomeClass from "./Component/HomeClass";
import { BrowserRouter as Router, Routes, Route, NavLink } from "react-router-dom";

function App() {
  return (
    <Router>
      {/* Navigation Bar */}
      <nav className="bg-gradient-to-r from-blue-500 to-purple-600 p-4 shadow-lg">
        <div className="container mx-auto flex justify-between items-center">
          {/* Logo */}
          <h1 className="text-white text-2xl font-bold">My Website</h1>
          
          {/* Navigation Links */}
          <div className="space-x-6">
            <NavLink 
              to="/" 
              className={({ isActive }) => 
                `text-white px-4 py-2 rounded-lg transition duration-300 ${
                  isActive ? "bg-white text-blue-600 shadow-md" : "hover:bg-white hover:text-blue-600"
                }`
              }
            >
              Home
            </NavLink>
            <NavLink 
              to="/about" 
              className={({ isActive }) => 
                `text-white px-4 py-2 rounded-lg transition duration-300 ${
                  isActive ? "bg-white text-blue-600 shadow-md" : "hover:bg-white hover:text-blue-600"
                }`
              }
            >
              About
            </NavLink>
            <NavLink 
              to="/contect" 
              className={({ isActive }) => 
                `text-white px-4 py-2 rounded-lg transition duration-300 ${
                  isActive ? "bg-white text-blue-600 shadow-md" : "hover:bg-white hover:text-blue-600"
                }`
              }
            >
              Contact
            </NavLink>
          </div>
        </div>
      </nav>

      {/* Page Content */}
      <div className="container mx-auto p-6">
        <Routes>
          <Route path="/" element={<HomeClass />} />
          <Route path="/about" element={<AboutFun />} />
          <Route path="/contect" element={<ContectFun />} />
        </Routes>
      </div>

      {/* Footer */}
      <FooterFun />
    </Router>
  );
}

export default App;
