import "./JobCardInfo.css";

type JobCardProp = {
	title: string;
	url: string;
	dateAdded: string;
	company: string;
};

function JobCardInfo({ title, dateAdded, company, url }: JobCardProp) {
	return (
		<div className="card-top">
			<div className="card-row">
				<a href={url} className="small text-left">
					{title}
				</a>
				<p className="small always-fit">{dateAdded}</p>
			</div>
			<p className="bold">{company}</p>
		</div>
	);
}

export default JobCardInfo;
