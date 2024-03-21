import "./JobCardEdit.css";
import { Offer } from "../App";
import { useState } from "react";

const API_BASE: string = import.meta.env.VITE_API_URL;

type JobCardEditProp = {
	setIsOfferAdded: React.Dispatch<React.SetStateAction<boolean>>;
	setIsEdit: React.Dispatch<React.SetStateAction<boolean>>;
	offer: Offer;
};

function JobCardEdit({ setIsEdit, offer, setIsOfferAdded }: JobCardEditProp) {
	const [errMessage, setErrMessage] = useState<string>("");

	const [newTitle, setNewTitle] = useState<string>(offer.title);
	const [isNewTitle, setIsNewTitle] = useState<boolean>(true);

	const [newCompany, setNewCompany] = useState<string>(offer.company);
	const [isNewCompany, setIsNewCompany] = useState<boolean>(true);

	const [newStatus, setNewStatus] = useState<string>(offer.status);
	const [isNewStatus, setIsNewStatus] = useState<boolean>(true);

	const [newDate, setNewDate] = useState<string>(offer.dateAdded);
	const [isNewDate, setIsNewDate] = useState<boolean>(true);

	function editJob(event: React.ChangeEvent<HTMLFormElement>) {
		event.preventDefault();

		if (!isNewCompany || !isNewTitle || !isNewStatus || !isNewDate) {
			return;
		}
		putData();
	}

	function putData() {
		fetch(`${API_BASE}/update-offer`, {
			method: "PUT",
			body: JSON.stringify({
				url: offer.url,
				status: newStatus,
				company: newCompany,
				dateAdded: newDate,
				title: newTitle,
			}),
			headers: {
				"Content-type": "application/json; charset=UTF-8",
			},
		})
			.then((response: Response) => response.json())
			.then((json) => {
				if (json["success"] === false) {
					setErrMessage(json["message"]);
					setIsOfferAdded(false);
				} else {
					setIsOfferAdded(true);
					setErrMessage("");
					setIsEdit(false);
				}
			});
	}

	function validateForm() {
		newTitle === "" ? setIsNewTitle(false) : setIsNewTitle(true);
		newCompany === "" ? setIsNewCompany(false) : setIsNewCompany(true);
		newStatus === "" ? setIsNewStatus(false) : setIsNewStatus(true);
		newDate === "" ? setIsNewDate(false) : setIsNewDate(true);
	}

	return (
		<>
			<div className="container">
				<form
					className="modal"
					onChange={validateForm}
					onKeyUp={validateForm}
					onSubmit={editJob}
				>
					<h2>Edit Job</h2>
					{errMessage !== "" ? <p>{errMessage}</p> : ""}
					<label htmlFor="title">Job Title:</label>
					<input
						name="title"
						type="text"
						defaultValue={newTitle}
						className={!isNewTitle ? "err" : ""}
						onChange={(e) => setNewTitle(e.target.value)}
					/>

					<label htmlFor="company">Company:</label>
					<input
						name="company"
						type="text"
						defaultValue={newCompany}
						className={!isNewCompany ? "err" : ""}
						onChange={(e) => setNewCompany(e.target.value)}
					/>

					<label htmlFor="status">Status:</label>
					<input
						name="status"
						type="text"
						defaultValue={newStatus}
						className={!isNewStatus ? "err" : ""}
						onChange={(e) => setNewStatus(e.target.value)}
					/>

					<label htmlFor="dateAdded">Date Applied:</label>
					<input
						name="dateAdded"
						type="text"
						defaultValue={newDate}
						className={!isNewDate ? "err" : ""}
						onChange={(e) => setNewDate(e.target.value)}
					/>

					<div className="row">
						<button className="submit-btn" type="submit">
							Submit
						</button>

						<button
							className="close-btn"
							onClick={() => setIsEdit(false)}
						>
							Close
						</button>
					</div>
				</form>
			</div>
		</>
	);
}

export default JobCardEdit;
