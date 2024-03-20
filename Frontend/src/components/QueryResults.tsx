import { Offer } from "../App";
import OfferAdder from "./OfferAdder";
import "./QueryResults.css";

type prop = {
	offersData: Offer[] | never[];
	setIsOfferAdded: React.Dispatch<React.SetStateAction<boolean>>;
	searchText: string;
};

function QueryResults({ offersData, searchText, setIsOfferAdded }: prop) {
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

	const filtered_data: Offer[] | never[] = filterOffers(
		offersData,
		searchText
	);

	return (
		<>
			{filtered_data.length > 0 ? (
				<main className="main">
					{filtered_data.map((offer) => (
						<QueryItem key={offer.url} offer={offer} />
					))}
				</main>
			) : (
				<OfferAdder setIsOfferAdded={setIsOfferAdded}></OfferAdder>
			)}
		</>
	);
}

function QueryItem({ offer }: { offer: Offer }) {
	const tagColorClass: string = getColor(offer);

	function getColor(offer: Offer) {
		let tagColor: string;
		offer.status === "Applied"
			? (tagColor = "tag-good")
			: offer.status === "Not Applied"
			? (tagColor = "tag-bad")
			: (tagColor = "tag-none");

		return tagColor;
	}

	return (
		<div className="card">
			<div className="card-row">
				<p>{offer.company}</p>
				<a href={offer.url}>{offer.title}</a>
			</div>
			<div className="card-row">
				<div className={"tag " + tagColorClass}>{offer.status}</div>
				<p>{offer.dateAdded}</p>
			</div>
		</div>
	);
}

export default QueryResults;
