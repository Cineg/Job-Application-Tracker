type NavbarSearchProps = {
	searchChange(event: React.ChangeEvent<HTMLInputElement>): void;
};

function NavbarSearch({ searchChange }: NavbarSearchProps) {
	return (
		<input
			className="search-bar"
			type="text"
			onChange={searchChange}
			placeholder="Search URLs, Company, Title..."
		></input>
	);
}

export default NavbarSearch;
