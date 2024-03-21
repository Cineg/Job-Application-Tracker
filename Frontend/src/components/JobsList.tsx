import { Offer } from "../App";
import JobCard from "./JobCard";
import OfferAdder from "./OfferAdder";
import "./JobsList.css";

type JobListProp = {
	filteredOffers: Offer[] | never[];
	setIsOfferAdded: React.Dispatch<React.SetStateAction<boolean>>;
};

function JobsList({ filteredOffers, setIsOfferAdded }: JobListProp) {
	return (
		<>
			{filteredOffers.length > 0 ? (
				<main className="main">
					{filteredOffers.map((offer) => (
						<JobCard
							key={offer.id}
							offer={offer}
							setIsOfferAdded={setIsOfferAdded}
						/>
					))}
				</main>
			) : (
				<OfferAdder setIsOfferAdded={setIsOfferAdded}></OfferAdder>
			)}
		</>
	);
}

export default JobsList;
