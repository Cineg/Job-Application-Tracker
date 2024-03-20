import { Offer } from "../App";
import JobCardInfo from "./JobCardInfo";
import "./JobCard.css";

function JobCard({ offer }: { offer: Offer }) {
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
			<JobCardInfo
				company={offer.company}
				dateAdded={offer.dateAdded}
				title={offer.title}
				url={offer.url}
				key={offer.id}
			/>

			<div className={"tag " + tagColorClass}>{offer.status}</div>
		</div>
	);
}

export default JobCard;
