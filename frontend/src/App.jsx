import { useState } from "react";
import { Routes, Route, BrowserRouter } from "react-router-dom";

import Header from "./views/base/Header";

import Login from "./views/auth/login";
import Register from "./views/auth/Register";
import CreatePassword from './views/auth/CreatePassword'
import ForgetPassword from './views/auth/ForgetPassword'
import Products from "./views/store/products";
import Dashboard from "./views/auth/Dashboard";
import Logout from "./views/auth/Logout";

function App() {
  const [count, setCount] = useState(0)

  return (
    <BrowserRouter>
      
        <Routes>
          <Route path="/login" element={<Login/>} />
          <Route path="register" element={<Register/>} />
          <Route path="/create-password" element={<CreatePassword/>} />
          <Route path="/forgot-password" element={<ForgetPassword />} />
          <Route path="/logout" element={<Logout/>} />
          <Route path="/" element={<Dashboard/>} />



          {/* Store Components */}
          <Route path="/" element={<Products/>} />
      
        </Routes>
    </BrowserRouter>
  )
}

export default App