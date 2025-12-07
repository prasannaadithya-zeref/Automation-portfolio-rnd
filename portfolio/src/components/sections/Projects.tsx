import { motion } from "framer-motion"
import { PROFILE } from "@/data/profile"
import { Card, CardContent, CardHeader, CardTitle, CardDescription, CardFooter } from "@/components/ui/card"
import { Badge } from "@/components/ui/badge"
import { Button } from "@/components/ui/button"
import { Github, FolderGit2 } from "lucide-react"

export const Projects = () => {
    return (
        <section id="projects" className="py-20 scroll-mt-16 bg-muted/30">
            <div className="container">
                <motion.div
                    initial={{ opacity: 0, y: 20 }}
                    whileInView={{ opacity: 1, y: 0 }}
                    viewport={{ once: true }}
                    transition={{ duration: 0.5 }}
                    className="space-y-8"
                >
                    <h2 className="text-3xl font-bold tracking-tight">Projects</h2>

                    <div className="grid md:grid-cols-2 lg:grid-cols-3 gap-6">
                        {PROFILE.projects.map((project, index) => (
                            <Card key={index} className="flex flex-col h-full hover:shadow-lg transition-shadow">
                                <CardHeader>
                                    <div className="mb-2 w-12 h-12 rounded-lg bg-primary/10 flex items-center justify-center text-primary">
                                        <FolderGit2 className="h-6 w-6" />
                                    </div>
                                    <CardTitle>{project.title}</CardTitle>
                                    <CardDescription className="line-clamp-2">
                                        {project.description}
                                    </CardDescription>
                                </CardHeader>
                                <CardContent className="flex-1">
                                    <div className="flex flex-wrap gap-2 mb-4">
                                        {project.tech.map((t) => (
                                            <Badge key={t} variant="secondary" className="text-xs">
                                                {t}
                                            </Badge>
                                        ))}
                                    </div>
                                </CardContent>
                                <CardFooter>
                                    <Button className="w-full gap-2" variant="outline" onClick={() => window.open(project.link, '_blank')}>
                                        <Github className="h-4 w-4" /> View Code
                                    </Button>
                                </CardFooter>
                            </Card>
                        ))}
                    </div>
                </motion.div>
            </div>
        </section>
    )
}
