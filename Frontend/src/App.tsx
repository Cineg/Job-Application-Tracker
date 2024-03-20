import { useEffect, useState } from "react";
import "./App.css";
import Navbar from "./components/Navbar";
import JobsList from "./components/JobsList";
import { fetchOffers } from "./hooks/fetch_offers";
import Spinner from "./components/Spinner";

export type Offer = {
	id: number;
	url: string;
	company: string;
	status: string;
	title: string;
	dateAdded: string;
};

function App() {
	const [searchText, setSearchText] = useState<string>("");
	const [offersData, setOffersData] = useState<Offer[] | Array<never>>([]);
	const [filteredOffers, setFilteredOffers] = useState<
		Offer[] | Array<never>
	>([]);

	const [isLoaded, setIsLoaded] = useState<boolean>(false);
	const [isOfferAdded, setIsOfferAdded] = useState<boolean>(false);

	useEffect(() => {
		fetchOffers().then((data) => {
			setOffersData(data);
			setFilteredOffers(data);
			setIsLoaded(true);
		});
	}, []);

	useEffect(() => {
		fetchOffers().then((data) => {
			setOffersData(data);
			setFilteredOffers(filterOffers(data, searchText));
		});
	}, [isOfferAdded]);

	useEffect(() => {
		searchText === ""
			? setFilteredOffers(offersData)
			: setFilteredOffers(filterOffers(offersData, searchText));
	}, [searchText]);

	function navbarSearch(text: string): void {
		setSearchText(text);
	}

	function filterOffers(
		offersData: Offer[] | never[],
		searchText: string
	): Offer[] {
		const filteredData: Offer[] = [];

		offersData.forEach((offer: Offer) => {
			if (
				offer.company.toLowerCase().includes(searchText) ||
				offer.title.toLowerCase().includes(searchText) ||
				offer.url.toLowerCase().includes(searchText)
			) {
				filteredData.push(offer);
			}
		});
		return filteredData;
	}

	return (
		<>
			<Navbar navbarSearch={navbarSearch}></Navbar>
			{!isLoaded ? (
				<div className="center">
					<Spinner />
				</div>
			) : (
				<JobsList
					filteredOffers={filteredOffers}
					setIsOfferAdded={setIsOfferAdded}
				/>
			)}
		</>
	);
}

export default App;
