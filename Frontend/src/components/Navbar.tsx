import "./Navbar.css";

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
			<input
				className="search-bar"
				type="text"
				onChange={searchChange}
				placeholder="Search URLs, Company, Title..."
			></input>
		</nav>
	);
}

export default Navbar;
