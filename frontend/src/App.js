import React from "react";
import Navbar from "./components/Navbar/Navbar";
import Footer from "./components/Footer/Footer";
import Home from "./pages/Home";
import Products from "./pages/Products";
import { Route, Routes } from "react-router-dom";
import About from "./pages/About";
import ProductDetails from "./pages/ProductDetails";

function App() {
  return (
    <div className="page--container">
      <Navbar />
      <div className="content--wrap">
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/products" element={<Products />} />
          <Route path="/about" element={<About />} />
          <Route path="/:pk/" element={<ProductDetails />} />
        </Routes>
      </div>
      <Footer />
    </div>
  );
}

export default App;