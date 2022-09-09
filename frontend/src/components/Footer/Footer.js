export default function Footer() {
  return (
    <div className="main--footer">
      <ul>
        <li>VK</li>
        <li>Twitter</li>
        <li>Discord</li>
        <li>Facebook</li>
      </ul>
      <p className="copyright">&#174; Dismal Gateways 2022</p>
      <img src={require("../images/dismal_logo_footer.png")}></img>
    </div>
  );
}
