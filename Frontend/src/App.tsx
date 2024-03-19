import { useEffect, useState } from "react";
import "./App.css";
import Navbar from "./components/Navbar";
import QueryResults from "./components/QueryResults";
import { fetchOffers } from "./hooks/fetch_offers";

export type Offer = {
	rowid: number;
	url: string;
	company: string;
	status: string;
	title: string;
	dateAdded: string;
};

export type OfferData = {
	offersData: Array<Offer>;
};

function App() {
	const [searchText, setSearchText] = useState<string>("");
	const [offersData, setOffersData] = useState<OfferData | Array<never>>([]);

	useEffect(() => {
		fetchOffers(setOffersData);
	}, []);

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
