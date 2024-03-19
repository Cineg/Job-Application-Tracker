import { Offer } from "../App";
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
	const tagColorClass: string = getColor(offer);

	function getColor(offer: Offer) {
		let tagColor: string;
		offer.Status === "Applied"
			? (tagColor = "tag-good")
			: offer.Status === "Not Applied"
			? (tagColor = "tag-bad")
			: (tagColor = "tag-none");

		return tagColor;
	}

	return (
		<div className="card">
			<div className="card-row">
				<p>{offer.CompanyName}</p>
				<a href={offer.URL}>{offer.PositionName}</a>
			</div>
			<div className="card-row">
				<div className={"tag " + tagColorClass}>{offer.Status}</div>
				<p>20/77/2137</p>
			</div>
		</div>
	);
}

export default QueryResults;
