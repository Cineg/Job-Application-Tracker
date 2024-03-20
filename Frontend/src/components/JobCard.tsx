import { Offer } from "../App";
import JobCardInfo from "./JobCardInfo";
import JobCardActions from "./JobCardActions";
import "./JobCard.css";

function JobCard({ offer }: { offer: Offer }) {
	const tagColorClass: string = "tag-" + getColor(offer);
	const borderColorClass: string = "border-" + getColor(offer);

	function getColor(offer: Offer) {
		let color: string;
		offer.status === "Applied"
			? (color = "good")
			: offer.status === "Not Applied"
			? (color = "bad")
			: (color = "none");

		return color;
	}

	return (
		<div className={"card " + borderColorClass}>
			<JobCardInfo
				company={offer.company}
				dateAdded={offer.dateAdded}
				title={offer.title}
				url={offer.url}
				key={offer.id}
			/>

			<div className="card-row">
				<JobCardActions
					status={offer.status}
					tagColorClass={tagColorClass}
				/>
			</div>
		</div>
	);
}

export default JobCard;
