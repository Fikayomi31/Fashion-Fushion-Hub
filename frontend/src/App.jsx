import { useState } from "react";
import { Routes, Route, BrowserRouter } from "react-router-dom";
import MainWrapper from "./layout/MainWrapper"

import Header from "./views/base/Header";
import Footer from "./views/base/Footer";
import Login from "./views/auth/login";
import Register from "./views/auth/Register";
import CreatePassword from './views/auth/CreatePassword'
import ForgetPassword from './views/auth/ForgetPassword'
import Products from "./views/store/products";
import Dashboard from "./views/auth/Dashboard";
import Logout from "./views/auth/Logout";
import ProductDetail from "./views/store/ProductDetail";




function App() {
  const [count, setCount] = useState(0)

  return (
    <BrowserRouter>
      {/*<Header />*/}

      <MainWrapper>
      
        <Routes>
          <Route path="/login" element={<Login/>} />
          <Route path="register" element={<Register/>} />
          <Route path="/create-password" element={<CreatePassword/>} />
          <Route path="/forgot-password" element={<ForgetPassword />} />
          <Route path="/logout" element={<Logout/>} />
          <Route path="/" element={<Dashboard/>} />



          {/* Store Components */}
          <Route path="/products" element={<Products/>} />
          <Route path="/detail/:slug/" element={<ProductDetail/>} />
      
        </Routes>
      </MainWrapper>
      <Footer />
      
    </BrowserRouter>
  )
}

export default App