import "./JobCardActions.css";

type JobCardActionsProp = {
	status: string;
	tagColorClass: string;
	setIsEdit: React.Dispatch<React.SetStateAction<boolean>>;
};

function JobCardActions({
	status,
	tagColorClass,
	setIsEdit,
}: JobCardActionsProp) {
	return (
		<>
			<div className={`tag ${tagColorClass}`}> {status} </div>
			<button
				className="tag tag-button edit"
				onClick={() => setIsEdit(true)}
			>
				Edit
			</button>
			<button className="tag tag-button delete">Delete</button>
		</>
	);
}

export default JobCardActions;
