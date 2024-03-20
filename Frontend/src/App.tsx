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

function App() {
	const [searchText, setSearchText] = useState<string>("");
	const [offersData, setOffersData] = useState<Offer[] | Array<never>>([]);
	const [isOfferAdded, setIsOfferAdded] = useState<boolean>(false);

	useEffect(() => {
		fetchOffers().then((data) => setOffersData(data));
	}, []);

	useEffect(() => {
		fetchOffers().then((data) => setOffersData(data));
	}, [isOfferAdded]);

	function navbarSearch(text: string): void {
		setSearchText(text);
	}

	return (
		<>
			<Navbar navbarSearch={navbarSearch}></Navbar>

			<QueryResults
				offersData={offersData}
				searchText={searchText}
				setIsOfferAdded={setIsOfferAdded}
			></QueryResults>
		</>
	);
}

export default App;
