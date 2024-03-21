import Modal from "./JobModal";
import "./JobCardDelete.css";
import { Offer } from "../App";
import { useEffect, useState } from "react";

type JobCardDeleteProp = {
	setIsDelete: React.Dispatch<React.SetStateAction<boolean>>;
	setIsOfferAdded: React.Dispatch<React.SetStateAction<boolean>>;
	offer: Offer;
};

const API_BASE: string = import.meta.env.VITE_API_URL;

function JobCardDelete({
	setIsDelete,
	setIsOfferAdded,
	offer,
}: JobCardDeleteProp) {
	const [deleteItem, setDeleteItem] = useState<boolean>(false);

	useEffect(() => {
		deleteOffer();
	}, [deleteItem]);

	function deleteOffer() {
		if (!deleteItem) {
			return;
		}
		deleteRequest();
		setIsDelete(false);
	}

	function deleteRequest() {
		fetch(`${API_BASE}/delete-offer`, {
			method: "DELETE",
			body: JSON.stringify({
				url: offer.url,
			}),
			headers: {
				"Content-type": "application/json; charset=UTF-8",
			},
		})
			.then((response: Response) => response.json())
			.then((json) => {
				if (json["success"] === false) {
					setIsOfferAdded(false);
				} else {
					setIsDelete(false);
					setIsOfferAdded(true);
				}
			});
	}

	return (
		<Modal>
			<div className="modal">
				<h2>Are sure you want to delete this item?</h2>
				<div className="offer-items">
					<p>
						<span className="row-name">Title</span>: {offer.title}
					</p>
					<p>
						<span className="row-name">Company</span>:{" "}
						{offer.company}
					</p>
					<p>
						<span className="row-name">Status</span>: {offer.status}
					</p>
					<p>
						<span className="row-name">Applied</span>:{" "}
						{offer.dateAdded}
					</p>
				</div>
				<div className="row">
					<button
						type="submit"
						className="submit-btn"
						onClick={() => setDeleteItem(true)}
					>
						Delete
					</button>

					<button
						className="close-btn"
						onClick={() => setIsDelete(false)}
					>
						Cancel
					</button>
				</div>
			</div>
		</Modal>
	);
}

export default JobCardDelete;
