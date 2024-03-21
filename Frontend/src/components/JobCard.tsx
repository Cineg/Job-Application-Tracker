import { Offer } from "../App";
import JobCardInfo from "./JobCardInfo";
import JobCardActions from "./JobCardActions";
import JobCardEdit from "./JobCardEdit";
import "./JobCard.css";
import { useState } from "react";

type JobCardProp = {
	offer: Offer;
	setIsOfferAdded: React.Dispatch<React.SetStateAction<boolean>>;
};

function JobCard({ offer, setIsOfferAdded }: JobCardProp) {
	const [isEdit, setIsEdit] = useState<boolean>(false);

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
					setIsEdit={setIsEdit}
				/>
			</div>

			{isEdit ? (
				<JobCardEdit
					setIsEdit={setIsEdit}
					offer={offer}
					setIsOfferAdded={setIsOfferAdded}
				/>
			) : (
				<></>
			)}
		</div>
	);
}

export default JobCard;
