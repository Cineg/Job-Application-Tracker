import { Offer } from "../App";

type prop = {
	offersData: Offer[];
	searchText: string;
};

function QueryResults({ offersData, searchText }: prop) {
	const filtered_data: Offer[] = [];
	offersData.forEach((offer) => {
		if (
			offer.CompanyName.toLowerCase().includes(searchText) ||
			offer.PositionName.toLowerCase().includes(searchText) ||
			offer.URL.toLowerCase().includes(searchText)
		) {
			filtered_data.push(offer);
		}
	});

	return (
		<div>
			{filtered_data.map((offer) => (
				<QueryItem key={offer.URL} offer={offer} />
			))}
		</div>
	);
}

function QueryItem({ offer }: { offer: Offer }) {
	return (
		<div className="">
			<a href={offer.URL}>
				{offer.CompanyName} -- {offer.PositionName}
			</a>
			<hr></hr>
			<p>{offer.Status}</p>
		</div>
	);
}

export default QueryResults;
