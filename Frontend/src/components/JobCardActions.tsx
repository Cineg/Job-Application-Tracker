import "./JobCardActions.css";

type JobCardActionsProp = {
	status: string;
	tagColorClass: string;
};

function JobCardActions({ status, tagColorClass }: JobCardActionsProp) {
	return (
		<>
			<div className={`tag ${tagColorClass}`}> {status} </div>
			<button className="tag tag-button edit">Edit</button>
			<button className="tag tag-button delete">Delete</button>
		</>
	);
}

export default JobCardActions;
