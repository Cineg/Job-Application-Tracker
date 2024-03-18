import { Offer, OfferData } from "../App";
import OfferAdder from "./OfferAdder";
import "./QueryResults.css";

type prop = {
	offersData: Offer[];
	searchText: string;
};

function QueryResults({ offersData, searchText }: prop) {
	function filterOffers(offersData: Offer[], searchText: string): Offer[] {
		const filteredData: Offer[] = [];
		offersData.forEach((offer: Offer) => {
			if (
				offer.CompanyName.toLowerCase().includes(searchText) ||
				offer.PositionName.toLowerCase().includes(searchText) ||
				offer.URL.toLowerCase().includes(searchText)
			) {
				filteredData.push(offer);
			}
		});
		return filteredData;
	}

	const filtered_data: Offer[] = filterOffers(offersData, searchText);

	return (
		<>
			{filtered_data.length > 0 ? (
				<main className="main">
					{filtered_data.map((offer) => (
						<QueryItem key={offer.URL} offer={offer} />
					))}
				</main>
			) : (
				<OfferAdder></OfferAdder>
			)}
		</>
	);
}

function QueryItem({ offer }: { offer: Offer }) {
	return (
		<div className="card">
			<a href={offer.URL}>
				{offer.CompanyName} -- {offer.PositionName}
			</a>
			<p>{offer.Status}</p>
		</div>
	);
}

export default QueryResults;
