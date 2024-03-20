import { useState } from "react";
import "./OfferAdder.css";
import NewOffer from "./NewOffer";

type offerAdderProp = {
	setIsOfferAdded: React.Dispatch<React.SetStateAction<boolean>>;
};

function OfferAdder({ setIsOfferAdded }: offerAdderProp) {
	const [errMessage, setErrMessage] = useState<string>("");

	return (
		<div className="wrapper">
			<p>
				Oops! Looks like there are no matches for this offer. Care to
				add one?
			</p>
			<NewOffer
				setErrMessage={setErrMessage}
				setIsOfferAdded={setIsOfferAdded}
			></NewOffer>
			{errMessage === "" ? (
				<></>
			) : (
				<p className="err-message">{errMessage}</p>
			)}
		</div>
	);
}

export default OfferAdder;
