import React, { useEffect, useState } from "react";

export default function Home() {
  const [offsetY, setoffsetY] = useState(0);
  const handleScroll = () => setoffsetY(window.pageYOffset);

  useEffect(() => {
    window.addEventListener("scroll", handleScroll);

    return () => window.removeEventListener("scroll", handleScroll);
  }, []);
  return (
    <div>
      <div className="wrapper--main">
        <img
          src={require("../components/images/castlelogo.png")}
          alt="castle--logo"
          className="background--img"
        ></img>
        <img
          src={require("../components/images/logo.png")}
          alt="logo"
          className="logo--img"
          style={{ transform: `translateY(${offsetY * 0.1}px)` }}
        ></img>
        <img
          src={require("../components/images/spear2.png")}
          alt="spear2--logo"
          className="spear2--img"
          style={{ transform: `translateY(${offsetY * 0.1}px)` }}
        ></img>
        <img
          src={require("../components/images/spear1.png")}
          alt="spear1--logo"
          className="spear1--img"
          style={{ transform: `translateY(${offsetY * 0.1}px)` }}
        ></img>
      </div>
    </div>
  );
}
