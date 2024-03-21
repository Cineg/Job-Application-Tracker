import { useState } from "react";
import "./NewOffer.css";

type newOfferProps = {
	setErrMessage: React.Dispatch<React.SetStateAction<string>>;
	setIsOfferAdded: React.Dispatch<React.SetStateAction<boolean>>;
};

const API_BASE: string = import.meta.env.VITE_API_URL;

function NewOffer({ setErrMessage, setIsOfferAdded }: newOfferProps) {
	const [companyName, setCompanyName] = useState<string>("");
	const [companyNameErr, setCompanyNameErr] = useState<boolean>(true);
	const [offerURL, setOfferURL] = useState<string>("");
	const [offerURLErr, setOfferURLErr] = useState<boolean>(true);
	const [positionName, setPositionName] = useState<string>("");
	const [positionNameErr, setPositionNameErr] = useState<boolean>(true);

	function formErr() {
		companyName === "" ? setCompanyNameErr(true) : setCompanyNameErr(false);
		offerURL === "" ? setOfferURLErr(true) : setOfferURLErr(false);
		positionName === ""
			? setPositionNameErr(true)
			: setPositionNameErr(false);
	}

	function postData() {
		fetch(`${API_BASE}/add-offer`, {
			method: "POST",
			body: JSON.stringify({
				company: companyName,
				title: positionName,
				url: offerURL,
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
				}
			});
	}

	function getFormData(event: React.ChangeEvent<HTMLFormElement>) {
		event.preventDefault();
		formErr();

		if (companyNameErr || offerURLErr || positionNameErr) {
			return;
		}

		postData();
	}

	return (
		<form
			className="form"
			onSubmit={getFormData}
			onChange={formErr}
			onKeyUp={formErr}
		>
			<div>
				<input
					placeholder="Provide Company Name"
					name="companyName"
					className={companyNameErr ? "input err" : "input"}
					onChange={(e) => {
						setCompanyName(e.target.value);
					}}
				></input>
				<input
					placeholder="Provide Offer URL"
					name="offerURL"
					className={offerURLErr ? "input err" : "input"}
					onChange={(e) => {
						setOfferURL(e.target.value);
					}}
				></input>
				<input
					placeholder="Provide Position Name"
					name="positionName"
					className={positionNameErr ? "input err" : "input"}
					onChange={(e) => {
						setPositionName(e.target.value);
					}}
				></input>
			</div>
			<button type="submit" className="button">
				Add
			</button>
		</form>
	);
}

export default NewOffer;
