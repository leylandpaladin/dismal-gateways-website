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
        <header className="container">
          <h2 className="main--title">For those who create music</h2>
          <img
            src={require("../components/images/full.png")}
            alt="full--logo"
            className="background--img"
            style={{ transform: `translateY(${offsetY * 0.5}px)` }}
          ></img>
          <img
            src={require("../components/images/earth.png")}
            alt="earth--logo"
            className="earth--img"
            style={{ transform: `translateY(${offsetY * 0.1}px)` }}
          ></img>
          <img
            src={require("../components/images/mount.png")}
            alt="mount--logo"
            className="mount--img"
            style={{ transform: `translateY(${offsetY * 0.1}px)` }}
          ></img>
        </header>
      </div>

      <div className="divider">
        <p className="divider--text">With love for Dungeon Synth</p>
      </div>

      <div className="about">
        <p className="about--text">
          Музыкальное издательство Dismal Gateways ориентируется на Black Metal
          и Dungeon Synth музыку. Глядя на беспрецедентный рост сцены «вширь» мы
          приняли решение брать под контроль качественную составляющую: пустых
          проектов (идеологически и музыкально) стало слишком много и теряется
          сама суть Черного Искусства – бескомпромиссность, интолерантность,
          идеология. Мы не хотим издавать всех подрядов ради того, чтобы кто-то
          мог закрыть свой гештальт (знаем, что это такое – проходили). Мы хотим
          быть вовлечены в творчество наших музыкантов равно также, как хотим,
          чтобы они сами были в него вовлечены. Мы взаимодействуем с
          музыкантами, даем критическую оценку, предлагаем помощь в графическом
          оформлении издания, производстве кассет и продвижении. В подобном
          творческом симбиозе и собираемся порождать черную магию. Enter the
          Dismal Gateways!
        </p>
        <img
          src={require("../components/images/main_second.png")}
          className="water--img"
        ></img>
      </div>
    </div>
  );
}
