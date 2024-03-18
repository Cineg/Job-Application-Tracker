import React, { useState } from "react";
import "./App.css";
import Navbar from "./components/Navbar";
import QueryResults from "./components/QueryResults";
import DB_MOCKUP from "./DB MOCKUP.json";

export type Offer = {
	URL: string;
	CompanyName: string;
	Status: string;
	PositionName: string;
};

export type OfferData = {
	offersData: Offer[];
};

function App() {
	const [searchText, setSearchText] = useState<string>("");
	const [offersData, setOffersData] = useState<OfferData>(
		DB_MOCKUP["Offers"]
	);

	function navbarSearch(text: string): void {
		setSearchText(text);
	}

	return (
		<>
			<Navbar navbarSearch={navbarSearch}></Navbar>
			<QueryResults
				offersData={offersData}
				searchText={searchText}
			></QueryResults>
		</>
	);
}

export default App;
