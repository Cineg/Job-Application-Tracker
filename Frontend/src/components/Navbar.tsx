import "./Navbar.css";
import NavbarSearch from "./NavbarSearch";

type NavbarSearch = {
	navbarSearch: (text: string) => void;
};

function Navbar({ navbarSearch }: NavbarSearch) {
	function searchChange(event: React.ChangeEvent<HTMLInputElement>) {
		navbarSearch(event.target.value);
	}

	return (
		<nav className="nav">
			<a href="/" className="logo">
				Logo
			</a>
			<NavbarSearch searchChange={searchChange} />
		</nav>
	);
}

export default Navbar;
