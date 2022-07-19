import { Link } from "react-router-dom";

export default function Navbar() {
  return (
    <nav className="navbar">
      <Link to="/">
        <img
          src={require("../images/nav_logo.png")}
          alt="nav--logo"
          className="nav--logo"
        ></img>
      </Link>
      <ul>
        <li>
          <button>
            <Link to="products">Products</Link>
          </button>
        </li>
        <li>
          <button>
            <Link to="about">About</Link>
          </button>
        </li>
      </ul>
    </nav>
  );
}
