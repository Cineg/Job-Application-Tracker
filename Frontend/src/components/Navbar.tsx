type NavbarSearch = {
	navbarSearch: (text: string) => void;
};

function Navbar({ navbarSearch }: NavbarSearch) {
	const nav_style: React.CSSProperties = {
		color: "red",
		padding: "1rem 0",
	};

	const search_style: React.CSSProperties = {
		minWidth: "80%",
		padding: ".5rem",
		borderRadius: "5px",
		border: "1px solid #1a1a1a",
	};

	function searchChange(event: React.ChangeEvent<HTMLInputElement>) {
		navbarSearch(event.target.value);
	}

	return (
		<nav style={nav_style}>
			<input
				style={search_style}
				type="text"
				onChange={searchChange}
				placeholder="Search URLs, Company, Title..."
			></input>
		</nav>
	);
}

export default Navbar;
