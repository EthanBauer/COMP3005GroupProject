CREATE TABLE IF NOT EXISTS events_halfend (
	event_id VARCHAR(50) PRIMARY KEY,
	match_suspended BOOLEAN,
	early_video_end BOOLEAN
);